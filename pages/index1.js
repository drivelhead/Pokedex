import Head from 'next/head'
import Image from 'next/image'
import { Inter } from 'next/font/google'
import ContactForm from '@/components/ContactForm'


const inter = Inter({ subsets: ['latin'] })

export default function Home(){
  return (
    <>
    <Head>
      <title>Code Lancashire</title>
      </Head>
      <div className="max-w-4xl mx-auto p-5">
<ContactForm />
      </div>
      </>
  )
}