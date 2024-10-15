using System;
using System.Diagnostics;
using UnityEngine;
using UnityEditor;
using Debug = UnityEngine.Debug;

namespace MU5.QuantumRendering.Editor
{
    public class ServerWindow : EditorWindow
    {
        const string DEFAULT_DATA_PATH = "Assets/MU5/QuantumRendering/Scripts/cs/Editor/ServerWindowData.asset";
        [SerializeField] ServerWindowData data;

        //ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        [MenuItem("Window/MU5/Server")]
        static void Open()
        {
            GetWindow<ServerWindow>("Server");
        }

        void OnEnable()
        {
            data = AssetDatabase.LoadAssetAtPath<ServerWindowData>(DEFAULT_DATA_PATH);
        }

        void OnGUI()
        {
            EditorGUILayout.BeginHorizontal(EditorStyles.toolbar);
            data = EditorGUILayout.ObjectField(data, typeof(ServerWindowData), false) as ServerWindowData;
            EditorGUILayout.EndHorizontal();

            if (data == null)
            {
                EditorGUILayout.LabelField("Please select ServerWindowData.");
            }
            else
            {
                EditorGUILayout.LabelField("Server Settings", EditorStyles.boldLabel);
                EditorGUILayout.Space(EditorGUIUtility.singleLineHeight);

                EditorGUILayout.LabelField("Python Path");
                data.python_path = EditorGUILayout.TextField(data.python_path);
                EditorGUILayout.Space(EditorGUIUtility.singleLineHeight);

                EditorGUILayout.LabelField("Server Application Path");
                data.server_application_path = EditorGUILayout.TextField(data.server_application_path);
                EditorGUILayout.Space(EditorGUIUtility.singleLineHeight);

                if (GUILayout.Button("Start"))
                {
#if UNITY_EDITOR_OSX
                    Debug.Log($"Server booting up with {data.python_path} {data.server_application_path}/app.py");
                    Process.Start(data.python_path, $"{data.server_application_path}");
#elif UNITY_EDITOR_WIN
                    Debug.LogWarning($"Windows is not supported.");
#endif
                }
                EditorGUILayout.Space(EditorGUIUtility.singleLineHeight);
            }
        }
    }
}