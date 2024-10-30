
# 0x01. Caching

## Project Overview

This project explores caching systems and different cache replacement algorithms. Caching systems are essential for optimizing data access times, reducing load, and enhancing overall system performance. Here, you’ll implement various cache replacement policies and gain insight into how they manage and optimize cache storage.

### Key Topics:
- Cache replacement policies: FIFO, LIFO, LRU, MRU, and LFU
- The purpose and limitations of a caching system

## Learning Objectives

By the end of this project, you should be able to:
- Describe what a caching system is and its purpose.
- Explain and implement the following cache replacement policies:
  - **FIFO** (First-In-First-Out)
  - **LIFO** (Last-In-First-Out)
  - **LRU** (Least Recently Used)
  - **MRU** (Most Recently Used)
  - **LFU** (Least Frequently Used)
- Recognize the limitations of caching systems, including constraints on cache size and data eviction policies.

## Project Structure

This project includes a base class `BaseCaching` that provides the foundation for creating caching classes with specific policies. All caching classes should inherit from `BaseCaching`, which defines:
- **MAX_ITEMS**: A limit on cache size.
- **cache_data**: A dictionary where cached data is stored.

### Files

- `base_caching.py`: Defines the `BaseCaching` class with core functionalities and constraints.
- **Additional caching classes**: Implement the different cache replacement algorithms as subclasses of `BaseCaching`.
- **Testing files**: Contains scripts to test each caching policy.

### Requirements

- **Python Version**: 3.7 (interpreted/compiled on Ubuntu 18.04 LTS)
- **Code Style**: `pycodestyle` (version 2.5)
- **Documentation**: All modules, classes, and methods must include documentation describing their purpose.
- **Executable Files**: All files must be executable.

## Cache Replacement Policies

1. **FIFO (First-In-First-Out)**:
   - Oldest items are removed first.
   
2. **LIFO (Last-In-First-Out)**:
   - Most recently added items are removed first.
   
3. **LRU (Least Recently Used)**:
   - The item that has not been accessed for the longest time is removed.
   
4. **MRU (Most Recently Used)**:
   - The most recently accessed item is removed.
   
5. **LFU (Least Frequently Used)**:
   - The item that has been accessed the least frequently is removed.

## Usage

Each caching policy class should implement the `put()` and `get()` methods:
- **`put(key, item)`**: Adds an item to the cache with the specified key.
- **`get(key)`**: Retrieves the item associated with the given key.

## Running the Code

To test the cache replacement policies, you can run the included scripts or create your own:

```bash
python3 <your_test_file.py>
```

Example:
```bash
python3 0-main.py
```

### Style Check

Ensure code style compliance using:
```bash
Get-ChildItem -Recurse -Filter *.py | ForEach-Object { python -m pycodestyle $_.FullName }
```

## Additional Information

- **Resources**:
  - [Cache replacement policies - FIFO](link)
  - [Cache replacement policies - LIFO](link)
  - [Cache replacement policies - LRU](link)
  - [Cache replacement policies - MRU](link)
  - [Cache replacement policies - LFU](link)

## Author
Toqa Ayman Jumaa