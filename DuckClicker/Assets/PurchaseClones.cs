using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PurchaseClones : MonoBehaviour
{
    [SerializeField]
    public int clonesPurchased;
    [SerializeField]

    private Text text;

    public void purchasedCount()
    {
        clonesPurchased++;
        text.text = clonesPurchased.ToString();
    }
}
