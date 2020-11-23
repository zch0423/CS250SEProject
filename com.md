# 1 this is not ID
I think that's a good idea but we'd have to investigate whether the return type can be changed without breaking backward compatibility.



# 2 this is not ID
Tentatively slated for 5.8 M1 solely for the purpose of _team discussion_.



# 3 this is not ID
If such a refactoring breaks the existing API, we could introduce new methods that a) delegate to the existing ones for the null-check and b) return the given values. Similar to [`Objects.requireNonNull`](https://docs.oracle.com/javase/8/docs/api/java/util/Objects.html#requireNonNull-T-) from the `java.util` package.



# 4 this is not ID
The proposal is analogous to the signature for `org.junit.platform.commons.util.Preconditions.notNull(T, String)`.



