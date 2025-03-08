<script setup>
import { onMounted } from "vue";
import Header from "../../components/Header/Header.vue";
import Vacancy from "../../components/Vacancy/Vacancy.vue";
import { useVacanciesStore } from "@/stores/vacanciesStore";
const vacanciesStore = useVacanciesStore();
import { useHead } from "@vueuse/head";

useHead({
  title: 'Питомник "Красная Гвоздика"',
  meta: [
    { name: "description", content: 'питомник растений "Красная Гвоздика"' },
    {
      name: "keywords",
      content:
        "цветы, растения, саженцы, кустарники, деревья, купить саженцы, купить растения",
    },
  ],
});

onMounted(() => {
  vacanciesStore.getVacancies();
});
</script>

<template>
  <Header />
  <section class="vacancies">
    <div class="container">
      <h3 class="vacancies__title title">Вакансии</h3>
      <div
        class="row row-cols-1 row-cols-md-3 g-4"
        v-if="vacanciesStore.vacancies"
        v-auto-animate
      >
        <div class="col" v-for="vacancy in vacanciesStore.vacancies">
          <Vacancy
            :title="vacancy.title"
            :salary="vacancy.salary"
            :schedule="vacancy.schedule"
            :education="vacancy.education"
            :experience="vacancy.experience"
            :contactsPhone="vacancy.contacts_phone"
            :contactsEmail="vacancy.contacts_email"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_vars" as *;
@use "../../assets/sytles/_mixins" as *;
.vacancies {
  padding-top: 50px;
  @include bg-section("../../assets/images/vacancies-bg.jpg");
  &__title {
    color: $white;
  }
}
</style>
