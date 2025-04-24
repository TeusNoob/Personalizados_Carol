import Image from "next/image"
import Link from "next/link"
import { ArrowRight, Heart, ShoppingCart } from "lucide-react"

import { Button } from "@/components/ui/button"
import { BottomNavigation } from "@/components/bottom-navigation"

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col bg-gray-50">
      <header className="sticky top-0 z-50 w-full border-b bg-white px-4 py-3 shadow-sm">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Image
              src="/placeholder.svg?height=32&width=32&text=C"
              alt="Logo"
              width={32}
              height={32}
              className="rounded-full bg-pink-100"
            />
            <span className="text-lg font-semibold text-pink-500">Personalizados da Carol</span>
          </div>
          <div className="flex items-center gap-3">
            <Button variant="ghost" size="icon" className="relative rounded-full">
              <ShoppingCart className="h-5 w-5 text-gray-500" />
              <span className="absolute -top-1 -right-1 flex h-4 w-4 items-center justify-center rounded-full bg-pink-500 text-[10px] font-medium text-white">
                0
              </span>
            </Button>
          </div>
        </div>
      </header>

      <main className="flex-1 overflow-auto pb-20">
        {/* Status Bar */}
        <div className="bg-pink-500 py-1 px-4 text-center">
          <p className="text-xs font-medium text-white">Frete grátis para compras acima de R$100</p>
        </div>

        {/* Hero Section */}
        <section className="w-full py-4">
          <div className="px-4">
            <div className="rounded-2xl overflow-hidden relative">
              <Image
                src="/placeholder.svg?height=180&width=400&text=Personalizados"
                alt="Templates digitais"
                width={400}
                height={180}
                className="w-full object-cover"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex flex-col justify-end p-4">
                <h1 className="text-xl font-bold text-white">Templates digitais e produtos personalizados</h1>
                <p className="text-sm text-white/90 mt-1 mb-3">Transforme suas ideias em realidade</p>
                <Button className="w-fit rounded-full bg-pink-500 hover:bg-pink-600 text-sm">
                  Ver produtos
                  <ArrowRight className="ml-1 h-3 w-3" />
                </Button>
              </div>
            </div>
          </div>
        </section>

        {/* Categories Section */}
        <section className="w-full py-4">
          <div className="px-4">
            <h2 className="mb-3 text-base font-semibold text-gray-800">Categorias</h2>
            <div className="flex gap-3 overflow-x-auto pb-2 scrollbar-hide">
              {["Templates", "Convites", "Agendas", "Planners", "Personalizados"].map((category) => (
                <div key={category} className="flex-none">
                  <Button
                    variant="outline"
                    className="rounded-full border-pink-200 bg-white text-pink-600 hover:bg-pink-50 hover:text-pink-700"
                  >
                    {category}
                  </Button>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Products Section */}
        <section id="produtos" className="w-full py-4">
          <div className="px-4">
            <div className="flex items-center justify-between mb-3">
              <h2 className="text-base font-semibold text-gray-800">Meus Produtos</h2>
              <Link href="/produtos" className="text-xs font-medium text-pink-500">
                Ver todos
              </Link>
            </div>
            <div className="grid grid-cols-2 gap-3">
              {[1, 2, 3, 4].map((item) => (
                <div key={item} className="group relative overflow-hidden rounded-xl bg-white shadow-sm">
                  <div className="aspect-square overflow-hidden">
                    <Image
                      src={`/placeholder.svg?height=150&width=150&text=Produto ${item}`}
                      alt={`Produto ${item}`}
                      width={150}
                      height={150}
                      className="object-cover w-full h-full"
                    />
                    <Button
                      size="icon"
                      variant="ghost"
                      className="absolute top-1 right-1 h-7 w-7 rounded-full bg-white/80 text-pink-500"
                    >
                      <Heart className="h-4 w-4" />
                    </Button>
                  </div>
                  <div className="p-2">
                    <h3 className="font-medium text-sm">Produto {item}</h3>
                    <div className="mt-1 flex items-center justify-between">
                      <span className="font-medium text-pink-600 text-sm">R$ {(49.99 + item * 10).toFixed(2)}</span>
                      <Button size="sm" className="h-7 w-7 rounded-full p-0 bg-pink-500 hover:bg-pink-600">
                        <ShoppingCart className="h-3 w-3" />
                      </Button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Templates Section */}
        <section className="w-full py-4">
          <div className="px-4">
            <div className="flex items-center justify-between mb-3">
              <h2 className="text-base font-semibold text-gray-800">Templates Digitais</h2>
              <Link href="/produtos" className="text-xs font-medium text-pink-500">
                Ver todos
              </Link>
            </div>
            <div className="grid grid-cols-2 gap-3">
              {[1, 2, 3, 4].map((item) => (
                <div key={item} className="group relative overflow-hidden rounded-xl bg-white shadow-sm">
                  <div className="aspect-square overflow-hidden">
                    <Image
                      src={`/placeholder.svg?height=150&width=150&text=Template ${item}`}
                      alt={`Template ${item}`}
                      width={150}
                      height={150}
                      className="object-cover w-full h-full"
                    />
                    <Button
                      size="icon"
                      variant="ghost"
                      className="absolute top-1 right-1 h-7 w-7 rounded-full bg-white/80 text-pink-500"
                    >
                      <Heart className="h-4 w-4" />
                    </Button>
                  </div>
                  <div className="p-2">
                    <h3 className="font-medium text-sm">Template Digital {item}</h3>
                    <div className="mt-1 flex items-center justify-between">
                      <span className="font-medium text-pink-600 text-sm">R$ {(19.99 + item).toFixed(2)}</span>
                      <Button size="sm" className="h-7 w-7 rounded-full p-0 bg-pink-500 hover:bg-pink-600">
                        <ShoppingCart className="h-3 w-3" />
                      </Button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Promotions Section */}
        <section className="w-full py-4">
          <div className="px-4">
            <h2 className="mb-3 text-base font-semibold text-gray-800">Promoções</h2>
            <div className="rounded-xl bg-gradient-to-r from-pink-500 to-pink-400 p-4 text-white">
              <h3 className="text-lg font-bold">Oferta Especial</h3>
              <p className="mt-1 text-sm text-white/90">
                Use o código CAROL20 e ganhe 20% de desconto em qualquer template!
              </p>
              <Button className="mt-3 bg-white text-pink-600 hover:bg-pink-50 rounded-full text-sm">Aproveitar</Button>
            </div>
          </div>
        </section>
      </main>

      <BottomNavigation />
    </div>
  )
}
