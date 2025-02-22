import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useGalleryStore = defineStore("galleryStore", () => {
    //states
    const galleryCategory = ref();
    const galleryImages = ref()

    //actions
    const getGalleryCategory = async () => {
        try {
            const { data } = await axios.get("/api/stockapp/gallery-categories/")
            galleryCategory.value = data.results;
        } catch(err){
            console.error(err);
        }
    }
    const getGalleryImagesByCategory = async (id) => {
        try {
            const { data } = await axios.get(`/api/stockapp/gallery-images/?category=${id}`)
            galleryImages.value = data.results;
        } catch(err){
            console.error(err);
        }
    }




    return{
        galleryCategory,
        galleryImages,
        getGalleryCategory,
        getGalleryImagesByCategory
    }
})