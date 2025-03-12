import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const usePlantsStore = defineStore("plantsStore", () => {
  //states
  const categories = ref();
  const genuses = ref();
  const plants = ref();
  const plant = ref();
  const isLoading = ref(false);
  const currentGenus = ref();
  const currentCategory = ref();
  const searchQuery = ref("");
  const isTableMode = ref(false);
  const pots = ref();
  const currentPot = ref();
  const currentPage = ref(1);
  const totalPages = ref(0);
  const isMounted = ref(false);

  //getters
  const searchPlants = computed(() => {
    if (plants.value && searchQuery.value) {
      const filtered = plants.value.filter((plant) =>
        plant.species.name
          .toLowerCase()
          .includes(searchQuery.value.toLowerCase())
      );
      return filtered;
    } else if (plants.value && searchQuery.value === "") {
      return plants.value;
    }
    return [];
  });

  const searchGenuses = computed(() => {
    if (genuses.value && searchQuery.value) {
      const filtered = genuses.value.filter((genus) =>
        genus.name.toLowerCase().includes(searchQuery.value.toLowerCase())
      );
      return filtered;
    } else if (genuses.value && searchQuery.value === "") {
      return genuses.value;
    }
    return [];
  });

  const genusName = computed(() => {
    if (!currentGenus.value || !genuses.value) {
      return "";
    }
    const genus = genuses.value.find((g) => g.id === currentGenus.value);
    return genus ? genus.name : "";
  });

  const categoryName = computed(() => {
    if (!currentCategory.value || !categories.value) {
      return "";
    }
    const category = categories.value.find(
      (c) => c.id === currentCategory.value
    );
    return category ? category.name : "";
  });

  //actions
  const throttling = (minLoadingTime = 300) => {
    isLoading.value = true;
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve();
      }, minLoadingTime);
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
  const getPlants = async () => {
    try {
      isLoading.value = true
      let allPlants = [];
      let uniquePlants = new Set();
      const filter = {
        category_id: currentCategory.value || "",
        genus_id: currentGenus.value || "",
        pot_size: currentPot.value || "",
        page: currentPage.value || 1,
        search: searchQuery.value || "",
      };

      const { data } = await axios.get(`/api/plantapp/plant/`, {
        params: {
          genus__category: filter.category_id,
          genus: filter.genus_id,
          page: filter.page,
          pot_size: filter.pot_size,
          search: filter.search,
        },
      });

      for (const plant of data.results) {
        const uniqueKey = `${plant.species.name}-${plant.min_price}-${plant.min_height}-${plant.min_pot_size}`;
        if (!uniquePlants.has(uniqueKey)) {
          uniquePlants.add(uniqueKey);
          allPlants.push(plant);
        }
      }

      totalPages.value = data.totalPages;
      plants.value = allPlants;
    } catch (err) {
      console.error(err);
    } finally {
      await throttling(300).then(() => {
        isLoading.value = false;
      });
      if (!isMounted.value) {
        isMounted.value = true;
      }
    }
  };
  const getPlantById = async (id) => {
    try {
      const { data } = await axios.get(`/api/plantapp/plant/${id}/`);
      plant.value = data;
    } catch (err) {
      console.error(err);
    }
  };

  const getPots = async () => {
    try {
      const { data } = await axios.get(`/api/stockapp/pot-sizes/`);
      const uniquePotSizes = new Set(data.map((item) => item.pot_size));
      const uniquePots = Array.from(uniquePotSizes).map((size) => ({
        pot_size: size,
      }));
      pots.value = uniquePots;
    } catch (err) {
      console.error(err);
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
    isMounted,
    currentCategory,
    currentGenus,
    searchPlants,
    searchQuery,
    isTableMode,
    getPots,
    pots,
    currentPot,
    searchGenuses,
    currentPage,
    totalPages,
    genusName,
    categoryName,
  };
});
