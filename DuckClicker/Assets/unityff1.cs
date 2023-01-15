using UnityEngine;
using System.Runtime.InteropServices;

public class NewBehaviourScript : MonoBehaviour {

    [DllImport("__Internal")]
    private static extern string UpdateLeaderboard(int score);

    [DllImport("__Internal")]
    private static extern string GetLeaderboard();

}