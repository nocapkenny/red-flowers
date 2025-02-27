import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const usePriceStore = defineStore("priceStore", () => {
    //states
    const prices = ref()

    //actions
    const getPrices = async () => {
        try {
            const { data } = await axios.get(`/api/stockapp/price-files/`)
            prices.value = data.results;
            console.log(prices.value)
        } catch(err){
            console.error(err);
        }
    }


    return{
        prices,
        getPrices
    }
})