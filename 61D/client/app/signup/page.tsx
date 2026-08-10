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

export default function SignUpPage() {
  return (
    <div className="bg-sky-50 min-h-screen flex items-center justify-center px-4">
      <Card className="w-full max-w-md">
        <CardHeader className="space-y-1">
          <CardTitle className="text-2xl font-bold">
            Створіть обліковий запис
          </CardTitle>
          <CardDescription>
            Введіть свої дані нижче аби створити обліковку
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="name">Повне ім&apos;я</Label>
              <Input id="name" placeholder="Онищенко Петро" required />
            </div>
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
              Зареєструватися
            </Button>
          </form>
          <div className="mt-4 text-center text-sm">
            Вже маєте обліковий запис?{" "}
            <Link href="/login" className="underline underline-offset-4">
              Увійдіть
            </Link>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
