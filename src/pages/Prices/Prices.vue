<script setup>
import Header from "../../components/Header/Header.vue";
import File from "../../components/File/File.vue";

const files = [
  "C:/Users/kenny300/Desktop/Programming/projects/red-flowers/backend/Прайс_многолетние_цветы_2022г_на_сайт.xls",
  "C:/Users/kenny300/Desktop/Programming/projects/red-flowers/backend/Прайс_деревья_2022.xls",
  "C:/Users/kenny300/Desktop/Programming/projects/red-flowers/backend/Прайс_кустарники_2022.xls",
  "C:/Users/kenny300/Desktop/Programming/projects/red-flowers/backend/Прайс_Мультиштамбы_2022.xls",
  "C:/Users/kenny300/Desktop/Programming/projects/red-flowers/backend/Прайс_Плодовые_деревья 2022г_на_сайт.xls",
];
const filePathsWithNames = files.map((filePath) => {
  const fileName = filePath.split("/").pop().split("\\").pop();
  return { filePath, fileName };
});
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
      <div class="prices__files" >
        <File
          v-for="file in filePathsWithNames"
          :key="file.filePath"
          :file-path="file.filePath"
          :file-name="file.fileName"
        />
      </div>
    </div>
  </div>
</template>

<style src="./Prices.scss" scoped />
