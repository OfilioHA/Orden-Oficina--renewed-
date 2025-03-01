import { Outlet } from 'react-router';
import { AliveProvider } from '@/providers/alive';

export function DefaultLayout() {
  return (
    <AliveProvider>
      <div id="layout-default">
        <main>
          <Outlet />
        </main>
      </div>
    </AliveProvider>
  );
}
