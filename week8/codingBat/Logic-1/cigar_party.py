def cigar_party(cigars, is_weekend):
    if cigars >= 40:
        if is_weekend:
            return True
        else:
            return cigars <= 60
    return False
