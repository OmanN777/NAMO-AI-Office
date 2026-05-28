import Link from 'next/link';

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-slate-950 text-white p-4">
      <h2 className="text-4xl font-bold mb-4">404 - Not Found</h2>
      <p className="text-slate-400 mb-8">The stock or agent data you&apos;re looking for doesn&apos;t exist.</p>
      <Link 
        href="/"
        className="px-6 py-3 bg-blue-600 hover:bg-blue-500 rounded-xl font-bold transition-all"
      >
        Back to Office
      </Link>
    </div>
  );
}
