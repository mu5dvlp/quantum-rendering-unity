using System;
using System.Net;
using System.Net.Sockets;
using UnityEngine;

//＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
namespace MU5.QuantumRendering.Runtime
{
    public class Broadcaster : MonoBehaviour
    {
        [SerializeField] string ip = "255.255.255.255";
        [SerializeField] int port = 8888;

        private UdpClient udpClient;

        //ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        void Start()
        {
            udpClient = new UdpClient();
        }

        public void Broadcast(byte[] data)
        {
            // UDPでブロードキャスト送信
            try
            {
                IPEndPoint endPoint = new IPEndPoint(IPAddress.Parse(ip), port);
                udpClient.Send(data, data.Length, endPoint);
            }
            catch (Exception ex)
            {
                Debug.LogError(ex);
                if (data != null) Debug.Log($"Data size: {data.Length}");
            }
        }

        void OnApplicationQuit()
        {
            udpClient.Close();
        }
    }
}