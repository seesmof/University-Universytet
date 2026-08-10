import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import Link from "next/link";

export default function LoginPage() {
  return (
    <div className="flex min-h-screen items-center justify-center px-4 bg-sky-50">
      <Card className="w-full max-w-md">
        <CardHeader className="space-y-1">
          <CardTitle className="text-2xl font-bold">Вітання</CardTitle>
          <CardDescription>
            Введіть свою електронну пошту та пароль аби ввійти
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="email">Електронна пошта</Label>
              <Input
                id="email"
                type="email"
                placeholder="mail@gmail.com"
                required
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Пароль</Label>
              <Input id="password" type="password" required />
            </div>
            <Button type="submit" className="w-full">
              Увійти
            </Button>
          </form>
          <div className="mt-4 text-center text-sm">
            Не маєте облікового запису?{" "}
            <Link href="/signup" className="underline underline-offset-4">
              Зареєструйтесь
            </Link>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
