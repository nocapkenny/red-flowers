<script setup>
const props = defineProps({
  isBigCard: {
    type: Boolean,
    default: false,
    required: true,
  },
});
</script>

<template>
  <div class="card">
    <img src="../../assets/images/1.jpg" class="card-img-top" alt="cardImg" />
    <div class="card-body">
      <h5 class="card-title">Роза</h5>
      <p class="card-text">Здесь описание этой розы</p>
      <div class="card__specs" v-if="isBigCard">
        <p class="card__spec"><span>Размер:</span> Большой</p>
        <p class="card__spec"><span>Солнце:</span> Full Sun</p>
        <p class="card__spec"><span>Вода:</span> Low</p>
        <p class="card__spec"><span>Высота:</span> 10см</p>
        <p class="card__spec"><span>Рост:</span> Быстрый</p>
      </div>
      <router-link class="btn btn-primary" to="">Узнать больше</router-link>
    </div>
  </div>
</template>

<style src="./Card.scss" scoped />
