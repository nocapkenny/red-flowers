import { ref } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const usePlantsStore = defineStore("plantsStore", () => {
  //states
  const categories = ref();
  const genuses = ref();
  const plants = ref();
  const plant = ref();
  const isLoading = ref(false);

  //actions
  const throttling = () => {
    //функция для искусственной задержки отображения компонента
    const minLoadingTime = 800;
    isLoading.value = true;
    const loadData = new Promise((resolve) => {
      setTimeout(() => {
        resolve();
      }, 2000);
    });
    Promise.all([
      loadData,
      new Promise((resolve) => setTimeout(resolve, minLoadingTime)),
    ]).then(() => {
      isLoading.value = false;
    });
  };

  const getCategories = async () => {
    try {
      const { data } = await axios.get("/api/plantapp/category/");
      categories.value = data.results.map((category) => ({
        id: category.id,
        name: category.name,
      }));
    } catch (err) {
      console.error(err);
    }
  };
  const getGenuses = async () => {
    try {
      let allGenuses = [];
      let page = 1;
      let hasMorePages = true;

      while (hasMorePages) {
        const { data } = await axios.get(`/api/plantapp/genus/?page=${page}`);
        const { results, next } = data;

        allGenuses = allGenuses.concat(
          results.map((genus) => ({
            id: genus.id,
            category_id: genus.category.id,
            name: genus.name,
          }))
        );

        if (next) {
          page++;
        } else {
          hasMorePages = false;
        }
      }
      const uniqueGenuses = allGenuses.reduce((acc, current) => {
        const isDuplicate = acc.some(
          (item) =>
            item.category_id === current.category_id &&
            item.name === current.name
        );

        if (!isDuplicate) {
          acc.push(current);
        }

        return acc;
      }, []);

      genuses.value = uniqueGenuses;
    } catch (err) {
      console.error(err);
    }
  };
  const getPlants = async (filter) => {
    try {
      const { data } = await axios.get(
        `/api/plantapp/plant/?page=1&genus__category=${filter.category_id}&genus=${filter.genus_id}`
      );
      plants.value = data.results;
    } catch (err) {
      console.error(err);
    } finally {
      throttling()
    }
  };
  const getPlantById = async (id) => {
    try {
      const { data } = await axios.get(`/api/plantapp/plant/${id}/`);
      plant.value = data;
    } catch (err) {
      console.error(err);
    } finally {
      console.log(plant.value);
    }
  };

  return {
    categories,
    getCategories,
    genuses,
    getGenuses,
    getPlants,
    plants,
    plant,
    getPlantById,
    isLoading,
  };
});
