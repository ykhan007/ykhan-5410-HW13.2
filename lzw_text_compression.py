import pickle

# ------------------------------
# 1. LZW Compression
# ------------------------------
def lzw_compress(uncompressed: str):
    # Clean text: remove characters outside basic 0–255 range
    # This avoids KeyError from strange unicode quotes/dashes etc.
    uncompressed = "".join(ch for ch in uncompressed if ord(ch) < 256)

    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    compressed_data = []

    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            # Only append if w is not empty (avoid KeyError for empty key)
            if w:
                compressed_data.append(dictionary[w])
            # Add new sequence to dictionary
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w if it is non-empty
    if w:
        compressed_data.append(dictionary[w])

    return compressed_data


# ------------------------------
# 2. LZW Decompression
# ------------------------------
def lzw_decompress(compressed):
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    # Pop first value and turn it into a string
    first = compressed.pop(0)
    w = chr(first)
    result = w

    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError("Bad compressed k: {}".format(k))

        result += entry
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry

    return result


# ------------------------------
# 3. Save compressed data using pickle
# ------------------------------
def save_pickle(data, filename="alice_compressed.pickle"):
    with open(filename, "wb") as f:
        pickle.dump(data, f)


# ------------------------------
# 4. Load compressed data using pickle
# ------------------------------
def load_pickle(filename="alice_compressed.pickle"):
    with open(filename, "rb") as f:
        return pickle.load(f)


# ------------------------------
# 5. MAIN PROGRAM
# ------------------------------
def main():
    # Load Alice text
    with open("alice.txt", "r", encoding="utf-8") as file:
        text = file.read()

    print("Original text length:", len(text))

    # Compress
    compressed = lzw_compress(text)
    print("Compressed length:", len(compressed))

    # Save compressed version
    save_pickle(compressed)

    # Load it again
    loaded_compressed = load_pickle()

    # Decompress
    decoded = lzw_decompress(loaded_compressed)

    print("\nFirst 45 characters of decoded text:")
    print(decoded[:45])


if __name__ == "__main__":
    main()
