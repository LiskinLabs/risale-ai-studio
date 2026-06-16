import type { Book } from '@/types/book';

export interface BuiltinBookEntry {
  filename: string;
  title: string;
  author: string;
  language: string;
  group: string;
  url?: string;
  coverFilename?: string;
}

export const BUILTIN_BOOKS: BuiltinBookEntry[] = [
  {
    filename: 'sozler.epub',
    title: 'Sözler',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Temel Eserler)',
  },
  {
    filename: 'mektubat.epub',
    title: 'Mektubat',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Temel Eserler)',
  },
  {
    filename: 'lemalar.epub',
    title: "Lem'alar",
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Temel Eserler)',
  },
  {
    filename: 'sualar.epub',
    title: 'Şuâlar',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Temel Eserler)',
  },
  {
    filename: 'tarihce-i-hayat.epub',
    title: 'Tarihçe-i Hayat',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Diğer Eserler)',
  },
  {
    filename: 'mesnevi-i-nuriye.epub',
    title: 'Mesnevî-i Nuriye',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Diğer Eserler)',
  },
  {
    filename: 'isaratul-icaz.epub',
    title: "İşaratü'l-İ'caz",
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Diğer Eserler)',
  },
  {
    filename: 'sikke-i-tasdik-i-gaybi.epub',
    title: 'Sikke-i Tasdik-i Gaybî',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Diğer Eserler)',
  },
  {
    filename: 'barla-lahikasi.epub',
    title: 'Barla Lâhikası',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Lâhikalar)',
  },
  {
    filename: 'kastamonu-lahikasi.epub',
    title: 'Kastamonu Lâhikası',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Lâhikalar)',
  },
  {
    filename: 'emirdag-lahikasi-1.epub',
    title: 'Emirdağ Lâhikası 1',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Lâhikalar)',
  },
  {
    filename: 'emirdag-lahikasi-2.epub',
    title: 'Emirdağ Lâhikası 2',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Lâhikalar)',
  },
  {
    filename: 'asa-yi-musa.epub',
    title: 'Asâ-yı Musa',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Diğer Eserler)',
  },
  {
    filename: 'muhakemat.epub',
    title: 'Muhakemat',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Külliyat (Diğer Eserler)',
  },
  {
    filename: 'sunuhat.epub',
    title: 'Sünûhat',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Eski Said Dönemi',
  },
  {
    filename: 'isarat.epub',
    title: 'İşârât',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Eski Said Dönemi',
  },
  {
    filename: 'tuluat.epub',
    title: 'Tulûât',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Eski Said Dönemi',
  },
  {
    filename: 'nurun-ilk-kapisi.epub',
    title: "Nur'un İlk Kapısı",
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Eski Said Dönemi',
  },
  {
    filename: 'nur-cesmesi.epub',
    title: 'Nur Çeşmesi',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Küçük Kitaplar ve Rehberler',
  },
  {
    filename: 'divan-i-harb-i-orfi.epub',
    title: 'Divan-ı Harb-i Örfî',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Eski Said Dönemi',
  },
  {
    filename: 'hutbe-i-samiye.epub',
    title: 'Hutbe-i Şamiye',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Küçük Kitaplar ve Rehberler',
  },
  {
    filename: 'munazarat.epub',
    title: 'Münazarat',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Eski Said Dönemi',
  },
  {
    filename: 'genclik-rehberi.epub',
    title: 'Gençlik Rehberi',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Küçük Kitaplar ve Rehberler',
  },
  {
    filename: 'hanimlar-rehberi.epub',
    title: 'Hanımlar Rehberi',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Küçük Kitaplar ve Rehberler',
  },
  {
    filename: 'konferans.epub',
    title: 'Konferans',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Küçük Kitaplar ve Rehberler',
  },
  {
    filename: 'tilsimlar.epub',
    title: 'Tılsımlar',
    author: 'Bediüzzaman Said Nursi',
    language: 'tr',
    group: 'Küçük Kitaplar ve Rehberler',
  },
];

export function getBuiltinBooksBaseUrl(): string {
  if (typeof window !== 'undefined') return `${window.location.origin}/builtin-books`;
  return process.env['NEXT_PUBLIC_BUILTIN_BOOKS_URL'] || 'http://localhost:3000/builtin-books';
}

export const BUILTIN_BOOKS_BASE_URL = '/builtin-books';
export function isBuiltinBook(book: Book): boolean {
  return book.builtin === true;
}
export function findBuiltinEntry(book: Book): BuiltinBookEntry | undefined {
  return BUILTIN_BOOKS.find(
    (entry) => book.builtin && (book.title === entry.title || book.sourceTitle === entry.filename),
  );
}
