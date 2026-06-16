import type { DictionaryProvider } from '../types';
import { BUILTIN_PROVIDER_IDS } from '../types';
import { stubTranslation as _ } from '@/utils/misc';
import { AppService } from '@/types/system';

interface LugatEntry {
  term: string;
  arabic: string | null;
  definition: string;
  [key: string]: any;
}

// ── IndexedDB helpers (reuses the same DB that meaningMode populates) ──

const IDB_NAME = 'risale-meaning-cache';
const IDB_STORE = 'terms';
const IDB_VERSION = 1;

function openIdb(): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(IDB_NAME, IDB_VERSION);
    req.onupgradeneeded = () => {
      req.result.createObjectStore(IDB_STORE, { keyPath: 'term' });
    };
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}

async function idbGet(term: string): Promise<LugatEntry | null> {
  try {
    const db = await openIdb();
    const tx = db.transaction(IDB_STORE, 'readonly');
    const store = tx.objectStore(IDB_STORE);
    const entry = await new Promise<{ term: string; definition: string } | undefined>(
      (resolve, reject) => {
        const r = store.get(term);
        r.onsuccess = () => resolve(r.result);
        r.onerror = () => reject(r.error);
      },
    );
    db.close();
    return entry ? { term: entry.term, arabic: null, definition: entry.definition } : null;
  } catch {
    return null;
  }
}

async function idbPrefix(prefix: string, limit: number): Promise<LugatEntry[]> {
  try {
    const db = await openIdb();
    const tx = db.transaction(IDB_STORE, 'readonly');
    const store = tx.objectStore(IDB_STORE);
    const all = await new Promise<{ term: string; definition: string }[]>((resolve, reject) => {
      const r = store.getAll();
      r.onsuccess = () => resolve(r.result as { term: string; definition: string }[]);
      r.onerror = () => reject(r.error);
    });
    db.close();
    return all
      .filter((e) => e.term.startsWith(prefix))
      .slice(0, limit)
      .map((e) => ({ term: e.term, arabic: null, definition: e.definition }));
  } catch {
    return [];
  }
}

async function idbInfix(infix: string, limit: number): Promise<LugatEntry[]> {
  try {
    const db = await openIdb();
    const tx = db.transaction(IDB_STORE, 'readonly');
    const store = tx.objectStore(IDB_STORE);
    const all = await new Promise<{ term: string; definition: string }[]>((resolve, reject) => {
      const r = store.getAll();
      r.onsuccess = () => resolve(r.result as { term: string; definition: string }[]);
      r.onerror = () => reject(r.error);
    });
    db.close();
    return all
      .filter((e) => e.term.includes(infix))
      .slice(0, limit)
      .map((e) => ({ term: e.term, arabic: null, definition: e.definition }));
  } catch {
    return [];
  }
}

async function idbHasData(): Promise<boolean> {
  try {
    const db = await openIdb();
    const tx = db.transaction(IDB_STORE, 'readonly');
    const store = tx.objectStore(IDB_STORE);
    const count = await new Promise<number>((resolve, reject) => {
      const r = store.count();
      r.onsuccess = () => resolve(r.result);
      r.onerror = () => reject(r.error);
    });
    db.close();
    return count > 0;
  } catch {
    return false;
  }
}

// ── Turkish normalization ───────────────────────────────────────────

const TR_SUFFIXES = [
  'larındaki',
  'lerindeki',
  'larından',
  'lerinden',
  'larında',
  'lerinde',
  'larına',
  'lerine',
  'larıyla',
  'leriyle',
  'larıdır',
  'leridir',
  'larımızdan',
  'lerimizden',
  'larımızda',
  'lerimizde',
  'larımıza',
  'lerimize',
  'larımızı',
  'lerimizi',
  'larımız',
  'lerimiz',
  'larınızdan',
  'lerinizden',
  'larınızda',
  'lerinizde',
  'larınıza',
  'lerinize',
  'larınızı',
  'lerinizi',
  'larınız',
  'leriniz',
  'larının',
  'lerinin',
  'larıma',
  'lerime',
  'larını',
  'lerini',
  'lardan',
  'lerden',
  'larda',
  'lerde',
  'lara',
  'lere',
  'ları',
  'leri',
  'lar',
  'ler',
  'maktandır',
  'mektendir',
  'maktan',
  'mekten',
  'makta',
  'mekte',
  'maktır',
  'mektir',
  'masından',
  'mesinden',
  'masında',
  'mesinde',
  'masına',
  'mesine',
  'masını',
  'mesini',
  'masıdır',
  'mesidir',
  'ması',
  'mesi',
  'makla',
  'mekle',
  'mak',
  'mek',
  'dıklarından',
  'diklerinden',
  'dıklarında',
  'diklerinde',
  'dıkları',
  'dikleri',
  'dıktan',
  'dikten',
  'duktan',
  'dükten',
  'dığından',
  'diğinden',
  'duğundan',
  'düğünden',
  'dığında',
  'diğinde',
  'duğunda',
  'düğünde',
  'dığını',
  'diğini',
  'duğunu',
  'düğünü',
  'dığıdır',
  'diğidir',
  'duğudur',
  'düğüdür',
  'dığı',
  'diği',
  'duğu',
  'düğü',
  'arak',
  'erek',
  'ınca',
  'ince',
  'unca',
  'ünce',
  'ıp',
  'ip',
  'up',
  'üp',
  'alı',
  'eli',
  'madan',
  'meden',
  'ımız',
  'imiz',
  'umuz',
  'ümüz',
  'ınız',
  'iniz',
  'unuz',
  'ünüz',
  'ının',
  'inin',
  'unun',
  'ünün',
  'ına',
  'ine',
  'una',
  'üne',
  'ım',
  'im',
  'um',
  'üm',
  'ın',
  'in',
  'un',
  'ün',
  'ı',
  'i',
  'u',
  'ü',
  'sı',
  'si',
  'su',
  'sü',
  'ndan',
  'nden',
  'ntan',
  'nten',
  'nda',
  'nde',
  'nta',
  'nte',
  'dan',
  'den',
  'tan',
  'ten',
  'da',
  'de',
  'ta',
  'te',
  'a',
  'e',
  'nın',
  'nin',
  'nun',
  'nün',
  'na',
  'ne',
  'nı',
  'ni',
  'nu',
  'nü',
  'yla',
  'yle',
  'la',
  'le',
  'dir',
  'dır',
  'dur',
  'dür',
  'tir',
  'tır',
  'tur',
  'tür',
  'lık',
  'lik',
  'luk',
  'lük',
  'sız',
  'siz',
  'suz',
  'süz',
  'lı',
  'li',
  'lu',
  'lü',
  'cı',
  'ci',
  'cu',
  'cü',
  'çı',
  'çi',
  'çu',
  'çü',
  'cık',
  'cik',
  'cuk',
  'cük',
  'ceğiz',
  'cağız',
  'ce',
  'ca',
  'çe',
  'ça',
  'ken',
  'ki',
  'kü',
  'deki',
  'daki',
  'teki',
  'taki',
  'ici',
  'ıcı',
  'ücü',
  'ucu',
  'ış',
  'iş',
  'uş',
  'üş',
];

function turkishNormalize(word: string): string[] {
  const candidates: string[] = [word];
  const lower = word.toLowerCase();

  const apostropheIdx = lower.indexOf("'");
  if (apostropheIdx > 0) {
    const after = lower.slice(0, apostropheIdx);
    if (after.length >= 3) candidates.push(after);
  }

  for (const suffix of TR_SUFFIXES) {
    if (lower.endsWith(suffix) && lower.length - suffix.length >= 3) {
      const stem = lower.slice(0, -suffix.length);
      const MUTATIONS: Record<string, string> = { ğ: 'k', b: 'p', c: 'ç', d: 't' };
      const last = stem[stem.length - 1];
      if (last && MUTATIONS[last]) {
        candidates.push(stem.slice(0, -1) + MUTATIONS[last]!);
      }
      if (stem.length >= 3) candidates.push(stem);
    }
  }

  return [...new Set(candidates)];
}

// ── Provider ─────────────────────────────────────────────────────────

export const createRisaleLugatProvider = (_appService: AppService): DictionaryProvider => {
  let useIdb: boolean | null = null;

  const lookupIdb = async (query: string): Promise<LugatEntry | null> => {
    // Step 1: exact
    let entry = await idbGet(query);
    if (entry) return entry;
    // Step 2: prefix
    if (query.length > 2) {
      const prefixed = await idbPrefix(query, 3);
      if (prefixed.length > 0) return prefixed[0]!;
    }
    // Step 3: normalized candidates
    if (query.length > 3) {
      for (const cand of turkishNormalize(query)) {
        if (cand === query || cand.length < 3) continue;
        entry = await idbGet(cand);
        if (entry) return entry;
        const prefixed = await idbPrefix(cand, 1);
        if (prefixed.length > 0) return prefixed[0]!;
      }
    }
    // Step 4: infix (slow but catches compounds)
    if (query.length > 4) {
      const infixed = await idbInfix(query, 1);
      if (infixed.length > 0) return infixed[0]!;
    }
    // Step 5: token-based fallback
    if (query.length > 3) {
      const tokens = query
        .split(/[\s\-',.!?]+/)
        .filter((t) => t.length >= 3)
        .slice(0, 3);
      for (const token of tokens) {
        entry = await idbGet(token);
        if (entry) return entry;
        entry = (await idbPrefix(token, 1))[0] ?? null;
        if (entry) return entry;
      }
    }
    return null;
  };

  return {
    id: BUILTIN_PROVIDER_IDS.risaleLugat,
    kind: 'builtin',
    label: _('Risale Lugat'),

    async lookup(word, ctx) {
      const query = word.toLowerCase();

      // Determine data source: use IndexedDB if it has data (web), fall
      // back to SQLite (Tauri) — determined once per session.
      if (useIdb === null) {
        useIdb = await idbHasData();
        if (!useIdb) {
          try {
            const db = await _appService.openDatabase('lugat', 'lugat.db', 'Data');
            const rows = await db.select<{ cnt: number }>('SELECT COUNT(*) as cnt FROM lugat');
            useIdb = !rows?.[0] || rows[0].cnt === 0;
            await db.close();
          } catch {
            useIdb = true; // SQLite unavailable → use IndexedDB
          }
        }
      }

      try {
        let entry: LugatEntry | null = null;

        if (useIdb) {
          entry = await lookupIdb(query);
        } else {
          // SQLite path — same multi-step logic as before
          const db = await _appService.openDatabase('lugat', 'lugat.db', 'Data');
          try {
            const level = ctx.dictionaryLevel ?? 3;
            const levelClause = level < 3 ? 'AND level >= ?' : '';

            let rows = await db.select<LugatEntry>(
              `SELECT term, arabic, definition FROM lugat WHERE term = ? ${levelClause} LIMIT 1`,
              level < 3 ? [query, level] : [query],
            );
            if ((!rows || rows.length === 0) && query.length > 2) {
              rows = await db.select<LugatEntry>(
                `SELECT term, arabic, definition FROM lugat WHERE term LIKE ? ${levelClause} LIMIT 3`,
                level < 3 ? [`${query}%`, level] : [`${query}%`],
              );
            }
            if ((!rows || rows.length === 0) && query.length > 3) {
              for (const cand of turkishNormalize(query)) {
                if (cand === query || cand.length < 3) continue;
                rows = await db.select<LugatEntry>(
                  `SELECT term, arabic, definition FROM lugat WHERE term = ? ${levelClause} LIMIT 1`,
                  level < 3 ? [cand, level] : [cand],
                );
                if (rows && rows.length > 0) break;
                rows = await db.select<LugatEntry>(
                  `SELECT term, arabic, definition FROM lugat WHERE term LIKE ? ${levelClause} LIMIT 1`,
                  level < 3 ? [`${cand}%`, level] : [`${cand}%`],
                );
                if (rows && rows.length > 0) break;
              }
            }
            if ((!rows || rows.length === 0) && query.length > 4) {
              rows = await db.select<LugatEntry>(
                `SELECT term, arabic, definition FROM lugat WHERE term LIKE ? ${levelClause} LIMIT 1`,
                level < 3 ? [`%${query}%`, level] : [`%${query}%`],
              );
            }
            if (rows && rows.length > 0) entry = rows[0]!;
          } finally {
            await db.close();
          }
        }

        if (!entry) return { ok: false, reason: 'empty' };

        const hgroup = document.createElement('hgroup');
        const h1 = document.createElement('h1');
        h1.textContent = entry.term;
        h1.className = 'text-lg font-bold';
        hgroup.append(h1);

        if (entry.arabic) {
          const arabicEl = document.createElement('p');
          arabicEl.textContent = entry.arabic;
          arabicEl.dir = 'rtl';
          arabicEl.className = 'text-2xl font-arabic text-right mt-2 mb-1';
          arabicEl.style.fontFamily = '"Traditional Arabic", "Scheherazade New", serif';
          hgroup.append(arabicEl);
        }

        ctx.container.append(hgroup);

        const defEl = document.createElement('div');
        defEl.className = 'mt-4 text-base leading-relaxed whitespace-pre-wrap';
        defEl.textContent = entry.definition;
        ctx.container.append(defEl);

        return {
          ok: true,
          headword: entry.term,
          sourceLabel: useIdb ? 'Risale-i Nur Lugatı' : 'Risale-i Nur Lugatı',
        };
      } catch (error) {
        console.error('Lugat lookup failed', error);
        return {
          ok: false,
          reason: 'error',
          message: error instanceof Error ? error.message : String(error),
        };
      }
    },
  };
};
