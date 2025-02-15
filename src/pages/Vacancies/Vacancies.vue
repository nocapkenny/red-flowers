<script setup>
import Header from "../../components/Header/Header.vue";
import Vacancy from "../../components/Vacancy/Vacancy.vue";

const vacancies = [1, 2, 3, 5];
</script>

<template>
  <Header />
  <div class="vacancies">
    <div class="container">
      <h3 class="vacancies__title title">Вакансии</h3>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col" v-for="vacancy in vacancies">
          <Vacancy />
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_vars" as *;
@use "../../assets/sytles/_mixins" as *;
.vacancies {
  @include bg-section("../../assets/images/vacancies-bg.jpg");
  &__title {
    color: $white;
  }
}
</style>
