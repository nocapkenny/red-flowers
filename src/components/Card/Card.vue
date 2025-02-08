<template>
  <!-- <div class="card">
        <img class="card__img" src="../../assets/images/1.jpg" alt="cardImg">
        <h3 class="card__title">Название</h3>
        <p class="card__descr">Описание</p>
        <div class="card__specs">
            <p class="card__spec"><span>Размер:</span> Большой</p>
            <p class="card__spec"><span>Солнце:</span> Full Sun</p>
            <p class="card__spec"><span>Вода:</span> Low</p>
            <p class="card__spec"><span>Высота:</span> 10см</p>
            <p class="card__spec"><span>Рост:</span> Быстрый</p>
        </div>
        <button class="card__btn">Узнать больше</button>
    </div> -->
  <div class="card" >
    <img src="../../assets/images/1.jpg" class="card-img-top" alt="cardImg" />
    <div class="card-body">
      <h5 class="card-title">Роза</h5>
      <p class="card-text">Здесь описание этой розы</p>
      <!-- <div class="card__specs">
        <p class="card__spec"><span>Размер:</span> Большой</p>
        <p class="card__spec"><span>Солнце:</span> Full Sun</p>
        <p class="card__spec"><span>Вода:</span> Low</p>
        <p class="card__spec"><span>Высота:</span> 10см</p>
        <p class="card__spec"><span>Рост:</span> Быстрый</p>
      </div> -->
      <router-link class="btn btn-primary" to="">Узнать больше</router-link>
    </div>
  </div>
</template>

<style src="./Card.scss" scoped />

