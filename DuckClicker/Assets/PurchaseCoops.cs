using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PurchaseCoops : MonoBehaviour
{
    [SerializeField]
    public int coopsPurchased;
    [SerializeField]

    private Text text;

    public void purchasedCount()
    {
        coopsPurchased++;
        text.text = coopsPurchased.ToString();
    }
}
