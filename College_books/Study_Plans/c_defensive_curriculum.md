# C Defensive Programming & Memory Management: An 8-Week Curriculum

## Phase 0: The Raw Metal Primer (Week 0)
This week focuses entirely on stripping away automated features (classes, namespaces) and getting comfortable with how raw C views the world. No dynamic memory (`malloc`/`free`) is allowed yet.

* **Day 1: Pure Data Structures**
  Build a `struct` representing a 2D physics particle (x, y, velocity, mass). Write a standalone function `update_particle(struct Particle *p)` that takes a pointer and modifies its values.
* **Day 2: The Truth About Strings (Null-Terminators)**
  Create two character arrays. Measure their length and glue them together into a third array using `strcpy` and `strcat` from `<string.h>`.
* **Day 3: Pointer Arithmetic and the Stack**
  Write a function that takes two integer pointers and swaps their values. Verify it worked by printing the original variables in `main()`.
* **Day 4: Multi-File Projects and Headers**
  Split the 2D particle code. Put the `struct` definition and function signatures in `physics.h`, the logic in `physics.c`, and `main()` in `main.c`.
* **Day 5: The Build System (Makefiles)**
  Write a basic `Makefile` inside your native Ubuntu Linux WSL2 workspace. Configure it so `make` compiles `main.c` and `physics.c` into a single executable.

## Phase 1: The Safety Nets (Weeks 1 & 2)
Set up the tripwires before writing complex logic.

* **Week 1: The Compiler and the Sanitizer**
  Write a program that intentionally leaks memory and reads outside an array boundary. Compile it using `gcc` with strict flags (`-Wall -Wextra -Werror -Wpedantic`). Compile again adding AddressSanitizer (`-fsanitize=address -g`) and learn to read the crash report.
* **Week 2: External Auditing with Valgrind**
  Write a program that allocates dynamic memory but forgets to free it. Run the compiled executable through Valgrind (`valgrind --leak-check=full ./your_program`). Learn to read the heap summary to trace leaks.

## Phase 2: Symmetrical Architecture (Weeks 3 & 4)
Unlearn destructors and automatic dropping, and start building manual, symmetrical memory structures.

* **Week 3: The Init/Cleanup Pattern**
  Build a dynamic array from scratch using raw structs. Write `my_array_init()` (calls `malloc`) and `my_array_destroy()` (calls `free` and sets pointer to `NULL`). Rule: Never allow a pointer to exist without initializing it to `NULL`.
* **Week 4: Opaque Pointers (Information Hiding)**
  Hide the contents of a `struct` in a `.c` file, only exposing a pointer in the `.h` file. Interacting with the data is only permitted through specific init/cleanup functions.

## Phase 3: Defensive Data Flows (Weeks 5 & 6)
Avoid dynamic memory allocation in the main loop to prevent fragmentation.

* **Week 5: Static Allocation and Ring Buffers**
  Design a circular buffer using a fixed block of memory allocated only once at startup. Write logic to overwrite oldest data when full, without calling `free()`.
* **Week 6: Error Handling without Exceptions**
  Refactor functions to return integer error codes (`0` for success, `-1` for failure). Pass data structures as double pointers (`**`) so functions can modify them while returning status.

## Phase 4: The Hardware Crucible (Weeks 7 & 8)
Run C on constrained hardware where memory bloat results in a hard crash.

* **Week 7: Bare-Metal Constraints**
  Port your ring buffer to a microcontroller board like the ESP32 using PlatformIO. Read sensor telemetry (like an MPU6050 IMU or GPS module) and push it into the buffer.
* **Week 8: Interrupts and Volatile Memory**
  Use the `volatile` keyword for variables changed by hardware timers or external module pulses. Practice safely sharing memory between the main loop and an interrupt service routine.

---

## The Daily Study Rhythm

1. **The Theory (15-20 Minutes):** Read up on the specific concept for the week. Focus purely on understanding the *why* before touching the keyboard.
2. **The Clean Build (30 Minutes):** Write a small, isolated script implementing the concept. Compile it cleanly using strict `gcc` flags. Do not move forward if there is a single warning.
3. **The Intentional Break (15 Minutes):** Deliberately violate the rule you just learned (e.g., remove `free()`, comment out the `NULL` assignment).
4. **The Autopsy (15 Minutes):** Compile and run the broken code using AddressSanitizer or Valgrind. Study the error output to train your eyes to recognize specific failures.
