**Is your feature request related to a problem? Please describe.**
The pydantic code calls `update_forward_refs()` on all classes at the end of the script. This method is deprecated in pydantic v2 and they recommend using `model_rebuild` 

https://docs.pydantic.dev/latest/concepts/models/#rebuild-model-schema

I don't know if this is to support pydantic v1 as well.

**Describe the solution you'd like**
Replace `update_forward_refs` by `model_rebuild`

**How important is this feature?** Select from the options below:
• Low - it's an enhancement but not crucial for work

**Additional context**

If 
