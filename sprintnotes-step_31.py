# === Stage 31: Add compact table rendering for long lists ===
# Project: SprintNotes
def compact_table(rows, headers=None):
    if rows and headers:
        col_widths = [len(h) for h in headers]
        for r in rows:
            for i, c in enumerate(r):
                col_widths[i] = max(col_widths[i], len(str(c)))
        fmt = '  '.join('{:<' + str(w) + ')' for w in col_widths)
        print(fmt.format(*headers))
        print('  '.join('-' * (w + 2) for w in col_widths))
        for r in rows:
            print(fmt.format(*r))
    else:
        for i, row in enumerate(rows):
            if i > 0:
                print()
            print('\t'.join(str(c).ljust(8) for c in row))
