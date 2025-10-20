import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Spam Detection App',
  description: 'AI-powered spam detection using machine learning',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
