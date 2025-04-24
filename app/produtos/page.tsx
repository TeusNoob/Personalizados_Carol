import Image from "next/image"
import Link from "next/link"
import { ArrowLeft, Heart, Search, ShoppingCart } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { BottomNavigation } from "@/components/bottom-navigation"

export default function ProdutosPage() {
  return (
    <div className="flex min-h-screen flex-col bg-gray-50">
      <header className="sticky top-0 z-50 w-full border-b bg-white px-4 py-3 shadow-sm">
        <div className="flex items-center gap-3">
          <Link href="/">
            <Button variant="ghost" size="icon" className="rounded-full">
              <ArrowLeft className="h-5 w-5 text-gray-500" />
            </Button>
          </Link>
          <div className="relative flex-1">
            <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-gray-400" />
            <Input
              placeholder="Buscar produtos"
              className="pl-9 rounded-full border-gray-200 bg-gray-100 focus-visible:ring-pink-500"
            />
          </div>
        </div>
      </header>

      <main className="flex-1 overflow-auto pb-20">
        <Tabs defaultValue="todos" className="w-full">
          <div className="sticky top-[57px] z-40 bg-white border-b shadow-sm">
            <TabsList className="w-full h-12 bg-white p-1">
              <TabsTrigger
                value="todos"
                className="flex-1 rounded-full data-[state=active]:bg-pink-500 data-[state=active]:text-white"
              >
                Todos
              </TabsTrigger>
              <TabsTrigger
                value="templates"
                className="flex-1 rounded-full data-[state=active]:bg-pink-500 data-[state=active]:text-white"
              >
                Templates
              </TabsTrigger>
              <TabsTrigger
                value="personalizados"
                className="flex-1 rounded-full data-[state=active]:bg-pink-500 data-[state=active]:text-white"
              >
                Personalizados
              </TabsTrigger>
            </TabsList>
          </div>

          <TabsContent value="todos" className="mt-0 px-4 py-4">
            <div className="grid grid-cols-2 gap-3">
              {Array.from({ length: 10 }).map((_, i) => (
                <div key={i} className="group relative overflow-hidden rounded-xl bg-white shadow-sm">
                  <div className="aspect-square overflow-hidden">
                    <Image
                      src={`/placeholder.svg?height=150&width=150&text=Produto ${i + 1}`}
                      alt={`Produto ${i + 1}`}
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
                    <h3 className="font-medium text-sm">Produto {i + 1}</h3>
                    <div className="mt-1 flex items-center justify-between">
                      <span className="font-medium text-pink-600 text-sm">R$ {(29.99 + i * 5).toFixed(2)}</span>
                      <Button size="sm" className="h-7 w-7 rounded-full p-0 bg-pink-500 hover:bg-pink-600">
                        <ShoppingCart className="h-3 w-3" />
                      </Button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </TabsContent>

          <TabsContent value="templates" className="mt-0 px-4 py-4">
            <div className="grid grid-cols-2 gap-3">
              {Array.from({ length: 6 }).map((_, i) => (
                <div key={i} className="group relative overflow-hidden rounded-xl bg-white shadow-sm">
                  <div className="aspect-square overflow-hidden">
                    <Image
                      src={`/placeholder.svg?height=150&width=150&text=Template ${i + 1}`}
                      alt={`Template ${i + 1}`}
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
                    <h3 className="font-medium text-sm">Template Digital {i + 1}</h3>
                    <div className="mt-1 flex items-center justify-between">
                      <span className="font-medium text-pink-600 text-sm">R$ {(19.99 + i).toFixed(2)}</span>
                      <Button size="sm" className="h-7 w-7 rounded-full p-0 bg-pink-500 hover:bg-pink-600">
                        <ShoppingCart className="h-3 w-3" />
                      </Button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </TabsContent>

          <TabsContent value="personalizados" className="mt-0 px-4 py-4">
            <div className="grid grid-cols-2 gap-3">
              {Array.from({ length: 4 }).map((_, i) => (
                <div key={i} className="group relative overflow-hidden rounded-xl bg-white shadow-sm">
                  <div className="aspect-square overflow-hidden">
                    <Image
                      src={`/placeholder.svg?height=150&width=150&text=Personalizado ${i + 1}`}
                      alt={`Personalizado ${i + 1}`}
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
                    <h3 className="font-medium text-sm">Personalizado {i + 1}</h3>
                    <div className="mt-1 flex items-center justify-between">
                      <span className="font-medium text-pink-600 text-sm">R$ {(49.99 + i * 10).toFixed(2)}</span>
                      <Button size="sm" className="h-7 w-7 rounded-full p-0 bg-pink-500 hover:bg-pink-600">
                        <ShoppingCart className="h-3 w-3" />
                      </Button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </TabsContent>
        </Tabs>
      </main>

      <BottomNavigation />
    </div>
  )
}
