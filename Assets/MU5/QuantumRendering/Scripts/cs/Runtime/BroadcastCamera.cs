using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
namespace MU5.QuantumRendering.Runtime
{
    [RequireComponent(typeof(Camera))]
    public class BroadcastCamera : MonoBehaviour
    {
        [SerializeField] Vector2Int size = new Vector2Int(256, 256);
        [SerializeField] float cycleTimeSec = 0.1f;
        [SerializeField] Broadcaster broadcaster;

        private Camera m_camera;

        //ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        void Awake()
        {
            m_camera = GetComponent<Camera>();
        }

        void Start()
        {
            InvokeRepeating(nameof(SendImageData), 0, cycleTimeSec);
        }

        void SendImageData()
        {
            // カメラのレンダリング結果をRenderTextureに保存
            RenderTexture renderTexture = new RenderTexture(size.x, size.y, 24);
            m_camera.targetTexture = renderTexture;
            Texture2D texture = new Texture2D(renderTexture.width, renderTexture.height, TextureFormat.RGB24, false);
            m_camera.Render();

            // RenderTextureをTexture2Dに変換
            RenderTexture.active = renderTexture;
            texture.ReadPixels(new Rect(0, 0, renderTexture.width, renderTexture.height), 0, 0);
            texture.Apply();
            RenderTexture.active = null;
            m_camera.targetTexture = null;

            // PNGとしてエンコード
            byte[] imageData = texture.EncodeToPNG();

            broadcaster.Broadcast(imageData);
        }
    }
}