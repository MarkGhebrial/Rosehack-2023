using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PurchaseEgg : MonoBehaviour
{
    [SerializeField]
    private int eggsPurchased;
    [SerializeField]

    private Text text;

    public void purchasedCount()
    {
        eggsPurchased++;
        text.text = eggsPurchased.ToString();
    }
}
