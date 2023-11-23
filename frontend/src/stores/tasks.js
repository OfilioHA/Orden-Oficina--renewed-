import { writable } from "svelte/store";

export const tasksPersonal = writable([]);
export const taskSelected = writable(null);
export const activeRound = writable(0);