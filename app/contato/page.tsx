import Link from "next/link"
import { ArrowLeft, Instagram, Mail, Phone, Send, PhoneIcon as WhatsApp } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Tabs } from '@/components/ui/tabs';
import { BottomNavigation } from "@/components/bottom-navigation"

export default function ContatoPage() {
  return (
    <div className="flex min-h-screen flex-col bg-gray-50">
      <header className="sticky top-0 z-50 w-full border-b bg-white px-4 py-3 shadow-sm">
        <div className="flex items-center gap-3">
          <Link href="/">
            <Button variant="ghost" size="icon" className="rounded-full">
              <ArrowLeft className="h-5 w-5 text-gray-500" />
            </Button>
          </Link>
          <h1 className="text-lg font-semibold text-gray-800">Contato</h1>
        </div>
      </header>

      <main className="flex-1 overflow-auto pb-20 px-4 py-4">
        <div className="space-y-6">
          <div className="rounded-xl bg-white p-4 shadow-sm">
            <h2 className="text-base font-semibold text-gray-800 mb-3">Fale Comigo</h2>
            <p className="text-sm text-gray-600 mb-4">Tem alguma dúvida ou pedido especial? Entre em contato!</p>

            <form className="space-y-4">
              <div className="space-y-2">
                <label htmlFor="name" className="text-sm font-medium text-gray-700">
                  Nome
                </label>
                <Input id="name" placeholder="Digite seu nome" className="rounded-lg border-gray-200" />
              </div>

              <div className="space-y-2">
                <label htmlFor="email" className="text-sm font-medium text-gray-700">
                  Email
                </label>
                <Input id="email" type="email" placeholder="Digite seu email" className="rounded-lg border-gray-200" />
              </div>

              <div className="space-y-2">
                <label htmlFor="message" className="text-sm font-medium text-gray-700">
                  Mensagem
                </label>
                <Textarea
                  id="message"
                  placeholder="Digite sua mensagem"
                  className="min-h-[120px] rounded-lg border-gray-200"
                />
              </div>

              <Button className="w-full rounded-full bg-pink-500 hover:bg-pink-600">
                Enviar mensagem
                <Send className="ml-2 h-4 w-4" />
              </Button>
            </form>
          </div>

          <div className="rounded-xl bg-white p-4 shadow-sm">
            <h2 className="text-base font-semibold text-gray-800 mb-3">Contato Direto</h2>

            <div className="space-y-3">
              <a
                href="https://wa.me/5500000000000"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-3 rounded-lg border border-gray-200 p-3 hover:bg-gray-50"
              >
                <div className="flex h-10 w-10 items-center justify-center rounded-full bg-green-500 text-white">
                  <WhatsApp className="h-5 w-5" />
                </div>
                <div>
                  <h3 className="font-medium text-sm">WhatsApp</h3>
                  <p className="text-xs text-gray-500">Resposta rápida</p>
                </div>
              </a>

              <a
                href="https://instagram.com/personalizadosdacarol"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-3 rounded-lg border border-gray-200 p-3 hover:bg-gray-50"
              >
                <div className="flex h-10 w-10 items-center justify-center rounded-full bg-gradient-to-tr from-purple-600 to-pink-500 text-white">
                  <Instagram className="h-5 w-5" />
                </div>
                <div>
                  <h3 className="font-medium text-sm">Instagram</h3>
                  <p className="text-xs text-gray-500">@personalizadosdacarol</p>
                </div>
              </a>

              <a
                href="mailto:contato@personalizadosdacarol.com"
                className="flex items-center gap-3 rounded-lg border border-gray-200 p-3 hover:bg-gray-50"
              >
                <div className="flex h-10 w-10 items-center justify-center rounded-full bg-pink-500 text-white">
                  <Mail className="h-5 w-5" />
                </div>
                <div>
                  <h3 className="font-medium text-sm">Email</h3>
                  <p className="text-xs text-gray-500">contato@personalizadosdacarol.com</p>
                </div>
              </a>

              <a
                href="tel:+5500000000000"
                className="flex items-center gap-3 rounded-lg border border-gray-200 p-3 hover:bg-gray-50"
              >
                <div className="flex h-10 w-10 items-center justify-center rounded-full bg-blue-500 text-white">
                  <Phone className="h-5 w-5" />
                </div>
                <div>
                  <h3 className="font-medium text-sm">Telefone</h3>
                  <p className="text-xs text-gray-500">(00) 00000-0000</p>
                </div>
              </a>
            </div>
          </div>

          <div className="rounded-xl bg-pink-50 p-4">
            <h2 className="text-base font-semibold text-pink-600 mb-2">Horário de Atendimento</h2>
            <p className="text-xs text-gray-600">
              Segunda a Sexta: 9h às 18h
              <br />
              Sábado: 9h às 13h
              <br />
              Domingo: Fechado
            </p>
          </div>
        </div>
      </main>

      <BottomNavigation />
    </div>
  )
}
