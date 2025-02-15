<script setup>
import Header from "../../components/Header/Header.vue";
import File from "../../components/File/File.vue";

const files = [1, 2, 3];
</script>

<template>
  <Header />
  <div class="prices">
    <div class="prices__box">
      <h3 class="prices__title title">Прайс-лист</h3>
      <p class="prices__text">
        Внимание! Уважаемые клиенты! В текущей ситуации цены, указанные на
        сайте, не являются официальной офертой: цены могут меняться в
        зависимости от ситуации на рынке. Чтобы выяснить актуальные цены,
        обращайтесь к специалистам питомника.
      </p>
      <div class="prices__files" v-for="file in files">
        <File />
      </div>
    </div>
  </div>
</template>

<style src="./Prices.scss" scoped/>

