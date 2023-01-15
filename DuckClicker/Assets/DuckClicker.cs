using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DuckClicker : MonoBehaviour
{
    [SerializeField]
    private int DuckCount;
    [SerializeField]
    private Text text;

    public void MakeADuck()
    {
        DuckCount += 5;
        text.text = DuckCount.ToString();
    }
}
