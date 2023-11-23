import { writable } from "svelte/store";

export const tasksPersonal = writable([]);
export const activeRound = writable(0);