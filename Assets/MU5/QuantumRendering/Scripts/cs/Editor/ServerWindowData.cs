using UnityEngine;

namespace MU5.QuantumRendering.Editor
{
    [CreateAssetMenu(menuName = "MU5/ServerWindowData")]
    public class ServerWindowData : ScriptableObject
    {
        public string python_path = $"{System.Environment.GetFolderPath(System.Environment.SpecialFolder.UserProfile)}/.pyenv/versions/3.11.6/bin/python";
        public string server_application_path = $"{Application.dataPath}/MU5/QuantumRendering/Scripts/python/app.py";
    }
}