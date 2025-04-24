"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"
import { Home, ShoppingBag, Gift, MessageSquare } from "lucide-react"
import { cn } from "@/lib/utils"

const navItems = [
  {
    name: "Início",
    href: "/",
    icon: Home,
  },
  {
    name: "Produtos",
    href: "/produtos",
    icon: ShoppingBag,
  },
  {
    name: "Variados",
    href: "/variados",
    icon: Gift,
  },
  {
    name: "Contato",
    href: "/contato",
    icon: MessageSquare,
  },
]

export function BottomNavigation() {
  const pathname = usePathname()

  return (
    <div className="fixed bottom-0 left-0 z-50 w-full border-t bg-white shadow-lg">
      <div className="mx-auto flex h-16">
        {navItems.map((item) => {
          const isActive = pathname === item.href
          return (
            <Link
              key={item.name}
              href={item.href}
              className={cn(
                "flex flex-1 flex-col items-center justify-center gap-1",
                isActive
                  ? "text-pink-500 after:absolute after:bottom-[calc(env(safe-area-inset-bottom)+3.5rem)] after:h-1 after:w-6 after:rounded-full after:bg-pink-500"
                  : "text-gray-500 hover:text-pink-500",
              )}
            >
              <item.icon className="h-5 w-5" />
              <span className="text-xs font-medium">{item.name}</span>
            </Link>
          )
        })}
      </div>
      <div className="h-[env(safe-area-inset-bottom)]" />
    </div>
  )
}
