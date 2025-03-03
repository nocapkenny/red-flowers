<script setup>
import Header from "../../components/Header/Header.vue";
import { useHead } from '@vueuse/head';

useHead({
  title: 'Питомник "Красная Гвоздика"',
  meta: [
    { name: 'description', content: 'питомник растений "Красная Гвоздика"' },
    { name: 'keywords', content: 'цветы, растения, саженцы, кустарники, деревья, купить саженцы, купить растения' },
  ]
});
</script>

<template>
  <Header />
  <div class="home">
    <h1 class="home__title">
      Добро пожаловать в питомник <br />
      Красная Гвоздика
    </h1>
    <router-link class="home__link" to="/catalog">Каталог</router-link>
  </div>
  <iframe
    src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d135655.90009497284!2d56.0062179!3d57.9094986!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x43e8a31d8d196b09%3A0xeec5bfe2c6e7e608!2z0JrRgNCw0YHQvdCw0Y8g0JPQstC-0LfQtNC40LrQsCwg0J_QuNGC0L7QvNC90LjQuiDQtNC10LrQvtGA0LDRgtC40LLQvdGL0YUg0Lgg0YHQsNC00L7QstGL0YUg0YDQsNGB0YLQtdC90LjQuQ!5e0!3m2!1sru!2sru!4v1739448670024!5m2!1sru!2sru"
    width="100%"
    height="450"
    style="border: 0"
    allowfullscreen=""
    loading="lazy"
    referrerpolicy="no-referrer-when-downgrade"
  ></iframe>
</template>

<style src="./Home.scss" scoped />
