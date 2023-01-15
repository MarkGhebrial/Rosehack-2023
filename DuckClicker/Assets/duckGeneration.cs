using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class duckGeneration : MonoBehaviour
{
    public DuckClicker scriptDuck;
    public PurchaseEgg scriptEgg;
    public PurchaseCoops scriptCoop;
    public PurchaseClones scriptClone;

    int eggMultiplier = 0;
    int coopMultiplier = 0;
    int cloneMultiplier = 0;

    public void duckMultipliers()
    {
        eggMultiplier = scriptEgg.eggsPurchased * 5;
        coopMultiplier = scriptCoop.coopsPurchased * 10;
        cloneMultiplier = scriptClone.clonesPurchased * 30;
    }

    float timePassed = 0.0f;
    void Update()
    {
        timePassed += Time.deltaTime;
        if (timePassed > 5f)
        {
            scriptDuck.DuckCount += scriptEgg.eggsPurchased + scriptCoop.coopsPurchased + scriptClone.clonesPurchased;
        }
    }
}
