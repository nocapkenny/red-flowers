import { ref } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const usePlantsStore = defineStore("plantsStore", () => {
  //states
  const categories = ref();
  const genuses = ref();

  //actions
  const getCategories = async () => {
    try {
      const { data } = await axios.get("/api/plantapp/category/");
      categories.value = data.results.map((category) => ({
        id: category.id,
        name: category.name,
      }));
    } catch (err) {
      console.error(err);
    } finally {
      console.log(categories.value);
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
    } finally {
      console.log(genuses.value);
    }
  };

  return { categories, getCategories, genuses, getGenuses };
});
