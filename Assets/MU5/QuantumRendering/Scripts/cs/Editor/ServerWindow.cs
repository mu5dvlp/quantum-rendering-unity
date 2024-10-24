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
            EditorGUI.BeginChangeCheck();

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
                    Debug.Log($"Server booting up with\nPython: {data.python_path}\nApplication: {data.server_application_path}");
                    Process.Start(data.python_path, $"{data.server_application_path}");
                }
                EditorGUILayout.Space(EditorGUIUtility.singleLineHeight);
            }

            if (EditorGUI.EndChangeCheck())
            {
                EditorUtility.SetDirty(data);
                AssetDatabase.Refresh();
                AssetDatabase.SaveAssets();
            }
        }
    }
}