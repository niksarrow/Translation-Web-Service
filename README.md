# Translation-Web-Service
Translation and Disfluency Removal Web Service

## References

### Generating Fluent Translations from Disfluent Text Without Access to Fluent References: IIT Bombay@IWSLT2020

[1] Nikhil Saini, Jyotsana Khatri, Preethi Jyothi, Pushpak Bhattacharyya
```
@inproceedings{saini-etal-2020-generating,
    title = "Generating Fluent Translations from Disfluent Text Without Access to Fluent References: {IIT} {B}ombay@{IWSLT}2020",
    author = "Saini, Nikhil  and
      Khatri, Jyotsana  and
      Jyothi, Preethi  and
      Bhattacharyya, Pushpak",
    booktitle = "Proceedings of the 17th International Conference on Spoken Language Translation",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.iwslt-1.22",
    doi = "10.18653/v1/2020.iwslt-1.22",
    pages = "178--186",
    abstract = "Machine translation systems perform reasonably well when the input is well-formed speech or text. Conversational speech is spontaneous and inherently consists of many disfluencies. Producing fluent translations of disfluent source text would typically require parallel disfluent to fluent training data. However, fluent translations of spontaneous speech are an additional resource that is tedious to obtain. This work describes the submission of IIT Bombay to the Conversational Speech Translation challenge at IWSLT 2020. We specifically tackle the problem of disfluency removal in disfluent-to-fluent text-to-text translation assuming no access to fluent references during training. Common patterns of disfluency are extracted from disfluent references and a noise induction model is used to simulate them starting from a clean monolingual corpus. This synthetically constructed dataset is then considered as a proxy for labeled data during training. We also make use of additional fluent text in the target language to help generate fluent translations. This work uses no fluent references during training and beats a baseline model by a margin of 4.21 and 3.11 BLEU points where the baseline uses disfluent and fluent references, respectively. Index Terms- disfluency removal, machine translation, noise induction, leveraging monolingual data, denoising for disfluency removal.",
}
```

### Disfluency Correction using Unsupervised and Semi-supervised Learning

[2] Nikhil Saini, Drumil Trivedi, Shreya Khare, Tejas Dhamecha, Preethi Jyothi, Samarth Bharadwaj, Pushpak Bhattacharyya
```
@inproceedings{saini-etal-2020-generating,
    title = "Disfluency Correction using Unsupervised and Semi-supervised Learning",
    author = "Saini, Nikhil  and
      Trivedi, Drumil and Khare, Shreya and Dhamecha, Tejas  and
      Jyothi, Preethi  and Bharadwaj, Samarth and
      Bhattacharyya, Pushpak",
    booktitle = "To appear in the Proceedings of EACL (16th Conference of the European Chapter of the Association for Computational Linguistics), 2021.",
    month = ,
    year = "2021",
    address = "Online",
    publisher = "EACL",
    url = "",
    doi = "",
    pages = "",
    abstract = "Spoken language is different from the written language in its style and structure. Disfluencies that appear in transcriptions from speech recognition systems generally hamper the performance of downstream NLP tasks. Thus, a disfluency correction system that converts disfluent to fluent text is of great value. This paper introduces a disfluency correction model that translates disfluent to fluent text by drawing inspiration from recent encoder-decoder unsupervised style-transfer models for text. We also show considerable benefits in performance when utilizing a small sample of 500 parallel disfluent-fluent sentences in a semisupervised way. Our unsupervised approach achieves a BLEU score of 79.39 on the Switchboard corpus test set, with further improvement to a BLEU score of 85.28 with semisupervision. Both are comparable to two competitive fully-supervised models.

",
}
```
## Contact

> Nikhil Saini
>
> Email : niksarrow196@gmail.com, nikhilra@cse.iitb.ac.in
>
> Department of Computer Science & Engineering 
>
> Indian Institute of Technology, Bombay

