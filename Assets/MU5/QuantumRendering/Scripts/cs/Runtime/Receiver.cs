using System.Net.Sockets;
using UnityEngine;
using UnityEngine.Events;

//＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
namespace MU5.QuantumRendering.Runtime
{
    public class Receiver : MonoBehaviour
    {
        [SerializeField] int listenPort = 8888;
        [SerializeField] UnityEvent<byte[]> onReceive;

        private UdpClient udpClient;

        //ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        void Start()
        {
            udpClient = new UdpClient(listenPort);
            StartListening();
        }

        async void StartListening()
        {
            while (true)
            {
                // 受信待ち
                UdpReceiveResult result = await udpClient.ReceiveAsync();
                byte[] data = result.Buffer;
                onReceive.Invoke(data);
            }
        }

        void OnApplicationQuit()
        {
            udpClient.Close();
        }
    }
}