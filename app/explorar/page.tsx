import Image from "next/image"
import { ArrowLeft, Search } from "lucide-react"
import Link from "next/link"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { BottomNavigation } from "@/components/bottom-navigation"

export default function ExplorePage() {
  return (
    <div className="flex min-h-screen flex-col bg-gray-50">
      <header className="sticky top-0 z-50 w-full border-b bg-white px-4 py-3">
        <div className="flex items-center gap-3">
          <Link href="/">
            <Button variant="ghost" size="icon" className="rounded-full">
              <ArrowLeft className="h-5 w-5 text-gray-500" />
            </Button>
          </Link>
          <div className="relative flex-1">
            <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-gray-400" />
            <Input
              placeholder="Buscar templates e produtos"
              className="pl-9 rounded-full border-gray-200 bg-gray-100 focus-visible:ring-pink-500"
            />
          </div>
        </div>
      </header>

      <main className="flex-1 overflow-auto pb-16 px-4 py-6">
        <h1 className="text-xl font-bold text-gray-800 mb-4">Explorar Categorias</h1>

        <div className="grid grid-cols-2 gap-4">
          {[
            { name: "Templates", image: "/placeholder.svg?height=150&width=150&text=Templates" },
            { name: "Convites", image: "/placeholder.svg?height=150&width=150&text=Convites" },
            { name: "Agendas", image: "/placeholder.svg?height=150&width=150&text=Agendas" },
            { name: "Planners", image: "/placeholder.svg?height=150&width=150&text=Planners" },
            { name: "Calendários", image: "/placeholder.svg?height=150&width=150&text=Calendários" },
            { name: "Personalizados", image: "/placeholder.svg?height=150&width=150&text=Personalizados" },
          ].map((category) => (
            <div key={category.name} className="group relative overflow-hidden rounded-xl bg-white shadow-sm">
              <div className="aspect-square overflow-hidden">
                <Image
                  src={category.image || "/placeholder.svg"}
                  alt={category.name}
                  width={150}
                  height={150}
                  className="object-cover w-full h-full"
                />
              </div>
              <div className="absolute inset-0 flex items-center justify-center bg-black/30">
                <h3 className="font-bold text-white text-lg">{category.name}</h3>
              </div>
            </div>
          ))}
        </div>

        <h2 className="text-xl font-bold text-gray-800 mt-8 mb-4">Mais Populares</h2>
        <div className="grid grid-cols-2 gap-3">
          {[1, 2, 3, 4].map((item) => (
            <div key={item} className="group relative overflow-hidden rounded-xl bg-white shadow-sm">
              <div className="aspect-square overflow-hidden">
                <Image
                  src={`/placeholder.svg?height=150&width=150&text=Popular ${item}`}
                  alt={`Item Popular ${item}`}
                  width={150}
                  height={150}
                  className="object-cover w-full h-full"
                />
              </div>
              <div className="p-2">
                <h3 className="font-medium text-sm">Item Popular {item}</h3>
                <div className="mt-1 flex items-center justify-between">
                  <span className="font-medium text-pink-600 text-sm">R$ {(29.99 + item * 5).toFixed(2)}</span>
                  <span className="text-xs text-gray-500">★★★★★</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </main>

      <BottomNavigation />
    </div>
  )
}
