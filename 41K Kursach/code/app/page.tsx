import { AppSidebar } from "@/components/app-sidebar";
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/components/ui/sidebar";

export default function Home() {
  return (
    <SidebarProvider>
      <AppSidebar />
      <SidebarInset>
        <div className="bg-gradient-to-br from-sky-50 min-h-screen p-3 flex items-center justify-center">
          <div className="max-w-xl mx-auto w-full">
            <SidebarTrigger />
          </div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  );
}
