using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
namespace MU5.QuantumRendering.Runtime
{
    public class ReceiveDisplay : MonoBehaviour
    {
        [SerializeField] Renderer m_renderer;
        [SerializeField] Vector2Int size = new Vector2Int(256, 256);

        private Texture2D receivedTexture;

        //ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        void Start()
        {
            receivedTexture = new Texture2D(size.x, size.y);
        }

        public void DisplayReceivedImage(byte[] data)
        {
            // 受信したバイトデータをPNG形式としてデコード
            receivedTexture.LoadImage(data);

            // 受信した画像をGameObjectのTextureとして表示
            m_renderer.material.mainTexture = receivedTexture;
        }
    }
}