<script setup>
import Header from "../../components/Header/Header.vue";
import Vacancy from "../../components/Vacancy/Vacancy.vue";

const vacancies = [1, 2, 3, 5];
</script>

<template>
  <Header />
  <div class="vacancies container">
    <h3 class="vacancies__title">Вакансии</h3>

    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div class="col" v-for="vacancy in vacancies">
        <Vacancy />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.vacancies {
  padding-top: 50px;
  padding-bottom: 50px;
  &__title {
    text-align: center;
    font-size: 32px;
    margin-bottom: 30px;
  }
}
</style>
