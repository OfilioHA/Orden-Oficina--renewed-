<script>
	import { fns, AppShell, Navbar, Header, Title, Divider } from '@svelteuidev/core';

	let isDark = false;
	let opened = false;

	function toggleTheme() {
		isDark = !isDark;
	}
	function toggleOpened() {
		opened = !opened;
	}
</script>

<AppShell>
    <main>
        <slot />
    </main>
</AppShell>
