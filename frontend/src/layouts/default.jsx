import { Outlet } from 'react-router';
import { AliveProvider } from '@/providers/alive';
import { SideBar } from '@/components/shared/side-bar';

export function DefaultLayout() {
  return (
    <AliveProvider>
      <div id="layout-default">
        <main className='d-flex'>
          <SideBar />
          <Outlet />
        </main>
      </div>
    </AliveProvider>
  );
}
