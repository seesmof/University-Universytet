<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar>
        <ion-title>Blank</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true">
      <ion-list>
        <ion-item>
          <ion-checkbox label-placement="end" justify="start">
            <h1>Create idea</h1>
            <ion-note>Run idea by brandy</ion-note>
          </ion-checkbox>
          <ion-badge color="success" slot="end">5 days</ion-badge>
        </ion-item>
        <ion-item>
          <ion-checkbox label-placement="end" justify="start">
            <h1>Learn ionic</h1>
            <ion-note>Get familiar with framework</ion-note>
          </ion-checkbox>
          <ion-badge color="primary" slot="end">2 weeks</ion-badge>
        </ion-item>
      </ion-list>

      <ion-fab vertical="bottom" horizontal="end" slot="fixed">
        <ion-fab-button @click="() => router.push('/new')">
          <ion-icon :icon="add"></ion-icon>
        </ion-fab-button>
      </ion-fab>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonBadge,
  IonCheckbox,
  IonContent,
  IonFab,
  IonFabButton,
  IonHeader,
  IonIcon,
  IonItem,
  IonList,
  IonNote,
  IonPage,
  IonTitle,
  IonToolbar,
} from "@ionic/vue";
import { add } from "ionicons/icons";
import { useRouter } from "vue-router";
const router = useRouter();
</script>

<style scoped>
#container {
  text-align: center;

  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
}

#container strong {
  font-size: 20px;
  line-height: 26px;
}

#container p {
  font-size: 16px;
  line-height: 22px;

  color: #8c8c8c;

  margin: 0;
}

#container a {
  text-decoration: none;
}
</style>
