import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useVacanciesStore = defineStore("vacanciesStore", () => {
  //states
  const vacancies = ref();

  //actions
  const getVacancies = async () => {
    try {
      const { data } = await axios.get("/api/docapp/vacancy/");
      vacancies.value = data.results;
    } catch (err) {
      console.error(err);
    }
  };


  return{
    vacancies,
    getVacancies
  }
});

