import Image from "next/image"
import Link from "next/link"
import { ArrowLeft, ExternalLink } from "lucide-react"
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Tabs } from '@/components/ui/tabs';
import { Button } from "@/components/ui/button"
import { BottomNavigation } from "@/components/bottom-navigation"

export default function VariadosPage() {
  return (
    <div className="flex min-h-screen flex-col bg-gray-50">
      <header className="sticky top-0 z-50 w-full border-b bg-white px-4 py-3 shadow-sm">
        <div className="flex items-center gap-3">
          <Link href="/">
            <Button variant="ghost" size="icon" className="rounded-full">
              <ArrowLeft className="h-5 w-5 text-gray-500" />
            </Button>
          </Link>
          <h1 className="text-lg font-semibold text-gray-800">Produtos Variados</h1>
        </div>
      </header>

      <main className="flex-1 overflow-auto pb-20 px-4 py-4">
        <div className="mb-6">
          <p className="text-sm text-gray-600 mb-4">
            Confira estes produtos incríveis de outros vendedores que eu recomendo!
          </p>
        </div>

        <div className="space-y-4">
          {[1, 2, 3, 4, 5].map((item) => (
            <div key={item} className="rounded-xl bg-white shadow-sm overflow-hidden">
              <div className="flex">
                <div className="w-1/3">
                  <Image
                    src={`/placeholder.svg?height=120&width=120&text=Afiliado ${item}`}
                    alt={`Produto Afiliado ${item}`}
                    width={120}
                    height={120}
                    className="object-cover w-full h-full"
                  />
                </div>
                <div className="w-2/3 p-3 flex flex-col justify-between">
                  <div>
                    <h3 className="font-medium text-sm">Produto Afiliado {item}</h3>
                    <p className="text-xs text-gray-500 mt-1">Vendedor Parceiro {item}</p>
                  </div>
                  <div className="flex items-center justify-between mt-2">
                    <span className="font-medium text-pink-600 text-sm">R$ {(39.99 + item * 15).toFixed(2)}</span>
                    <Button size="sm" className="rounded-full bg-pink-500 hover:bg-pink-600 text-xs h-8 px-3">
                      Ver na loja
                      <ExternalLink className="ml-1 h-3 w-3" />
                    </Button>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>

        <div className="mt-6 rounded-xl bg-pink-50 p-4">
          <h2 className="text-base font-semibold text-pink-600 mb-2">Parceria</h2>
          <p className="text-xs text-gray-600">
            Estes são produtos de vendedores parceiros. Ao comprar através dos links, você apoia o meu trabalho e ainda
            ganha produtos incríveis!
          </p>
        </div>
      </main>

      <BottomNavigation />
    </div>
  )
}
